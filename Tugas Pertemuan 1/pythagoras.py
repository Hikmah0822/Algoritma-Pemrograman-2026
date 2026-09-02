import math

def hitung_hipotenusa(a: float, b: float):
    """
    Fungsi untuk menghitung hipotenusa segitiga siku-siku
    berdasarkan Teorema Pythagoras.
    """
    if a <= 0 or b <= 0:
        return "Error: Panjang sisi segitiga harus lebih besar dari nol."
    
    c = math.sqrt(a**2 + b**2)
    return c

if __name__ == "__main__":
    print("=== Program Penghitung Sisi Miring (Pythagoras) ===")
    
    try:
        sisi_a = float(input("Masukkan panjang sisi alas (a): "))
        sisi_b = float(input("Masukkan panjang sisi tegak (b): "))
        
        hasil = hitung_hipotenusa(sisi_a, sisi_b)
        
        if isinstance(hasil, str):
            print(hasil)
        else:
            print(f"Panjang sisi miring (c) adalah: {hasil:.2f}")
            
    except ValueError:
        print("Error: Input harus berupa angka.")