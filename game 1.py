import random
import time

def generate_question():
    """Membangkitkan pertanyaan penjumlahan dengan dua angka acak."""
    num1 = random.randint(11, 99)
    num2 = random.randint(11, 99)
    return num1, num2

def main():
    print("Selamat datang di Game Penjumlahan Cepat!")
    print("Anda akan diberikan 10 pertanyaan penjumlahan dua angka.")
    print("Jawab secepat dan seakurat mungkin!")
    input("Tekan Enter untuk memulai...")
    print()

    total_questions = 10
    correct_answers = 0
    start_time = time.time()

    for i in range(total_questions):
        num1, num2 = generate_question()
        correct_answer = num1 + num2

        # Tampilkan pertanyaan dan minta jawaban pemain
        print(f"Pertanyaan {i+1}: {num1} + {num2} = ?")
        user_answer = input("Jawaban Anda: ")

        # Periksa apakah jawaban benar
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Jawaban Anda benar!")
            correct_answers += 1
        else:
            print("Jawaban Anda salah.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nGame selesai!")
    print(f"Total pertanyaan: {total_questions}")
    print(f"Jawaban benar: {correct_answers}")
    print(f"Jawaban salah: {total_questions - correct_answers}")
    print(f"Waktu yang dibutuhkan: {elapsed_time:.2f} detik")

if __name__ == "__main__":
    main()
    