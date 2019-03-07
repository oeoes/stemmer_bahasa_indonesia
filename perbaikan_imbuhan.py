import re
import kbbi as st


class PerbaikanImbuhan(st.Kbbi):

    """
    Lihat aturan peleburan pada file stemming_me.py
    fungsi ini dimaksudkan untuk mengubah huruf yang melebur kedalam huruf aslinya
    misal: memakai -> me-makai -> me-pakai -> sehingga didapat kata dasarnya 'pakai'
    """
    def peleburan_kata(self, awalan, akhiran, kata):
        res = re.findall(awalan+r'(\w+)'+akhiran, kata)
        if awalan is 'meng':
            if not self.periksa_kata(res[0]):
                return 'k'
            return ''
        # karena imbuhan meny mayoritasnya melebur, jadi tidak perlu menggukan kbbi untuk validasi
        elif awalan is 'meny':
            if re.match(awalan + r'[aiueo]', kata):
                return 's'
            return ''
        elif awalan is 'men':
            if not self.periksa_kata(res[0]):
                return 't'
            return ''
        elif awalan is 'mem':
            if not self.periksa_kata(res[0]):
                return 'p'
            return ''

    """
    Suatu kata yang disertai imbuhan secara morfologi ada yang terlihat melebur, ada juga yang memang itu huruf/kata 
    aslinya. Fungsi ini digunakan untuk memeriksa apakah kata hasil stemm ada pada KBBI bila ada berarti kata itu 
    memang bentuknya seperti itu (tidak melebur sama sekali). Bila tidak, maka huruf yang melebur akan digantikan 
    dengan huruf yang bersesuaian (lihat aturan peleburan)
    """
    # @param
    # ekspansi_imbuhan : mem-kan, maka imbuhan_dasarnya adalah me-kan
    # hasil_id (hasil imbuhan dasar) -> kata yg dipotong setelah imbuhan (dasar). misal -> me-mbangun-kan -> has_id = mbangun
    # hasil_ei (hasil ekspansi imbuhan) -> kata yang dipotong setelah imbuhan (kembangan), misal -> mem-bangun-kan -> has_ei = bangun
    def lebur_or_asli(self, hasil_ei, hasil_id, imbuhan_dasar, ekspansi_imbuhan, kata, awalan, akhiran=''):
        if self.periksa_kata(hasil_id):
            self.me_classification.get(imbuhan_dasar).append(kata)
            self.me_stemm.get(imbuhan_dasar).append(hasil_id)
            self.me_katdas.get(imbuhan_dasar).append(hasil_id)
        else:
            self.me_classification.get(ekspansi_imbuhan).append(kata)
            self.me_stemm.get(ekspansi_imbuhan).append(hasil_ei)
            self.me_katdas.get(ekspansi_imbuhan).append(
                str(self.peleburan_kata(awalan, akhiran, kata)) + ''.join(re.findall(awalan+r'(\w+)'+akhiran, kata)))

    """
    Bila kata tidak berpotensi melebur, kata itu bisa langsung disimpan ke dalam dictionary imbuhan terkait
    """
    # @oaram imbuhan, kata, awalan, akhiran (defaultnya kosong)
    def store_to_dict(self, imbuhan, kata, awalan, akhiran=''):
        self.me_classification.get(imbuhan).append(kata)
        self.me_stemm.get(imbuhan).append(*re.findall(awalan+r'(\w+)'+akhiran, kata))
        self.me_katdas.get(imbuhan).append(*re.findall(awalan+r'(\w+)'+akhiran, kata))
