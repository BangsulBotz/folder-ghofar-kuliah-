import random

def generate_puzzle():
    # Menghasilkan angka acak untuk teka-teki
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Menghasilkan operator acak
    operator = random.choice(['+', '-', 'x'])  # Penjumlahan, pengurangan, atau perkalian
    
    # Menghasilkan teka-teki
    if operator == '+':
        puzzle = f"{num1} tambah {num2}"
        answer = num1 + num2
    elif operator == '-':
        puzzle = f"{num1} kurang {num2}"
        answer = num1 - num2
    else:
        puzzle = f"{num1} kali {num2}"
        answer = num1 * num2
    
    return puzzle, answer

def main():
    print("Selamat datang di Game Tebak Matematika!")
    score = 0
    num_questions = 5
    
    for _ in range(num_questions):
        # Menghasilkan teka-teki baru
        puzzle, correct_answer = generate_puzzle()
        
        # Meminta pemain untuk memecahkan teka-teki
        print("Tebak teka-teki ini:")
        print(puzzle)
        user_answer = input("Masukkan jawaban Anda: ")
        
        # Memeriksa apakah jawaban benar
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Benar!")
            score += 1
        else:
            print(f"Salah! Jawaban yang benar adalah {correct_answer}.")
    
    print(f"Permainan selesai! Skor akhir Anda adalah {score} dari {num_questions}.")

if __name__ == "__main__":
    main()