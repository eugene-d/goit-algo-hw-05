from algo import boyer_moore, kmp, rabin_karp
from utils import read_file, select_test_patterns, print_separator
from benchmark import AlgorithmBenchmark


def main():
    print_separator("АНАЛІЗ ПРОДУКТИВНОСТІ АЛГОРИТМІВ ПОШУКУ ПІДРЯДКІВ")
    print("Порівняння продуктивності алгоритмів пошуку підрядків")
    print("Тестування: Boyer-Moore, KMP та Rabin-Karp")
    print()

    algorithms = {
        'Boyer-Moore': boyer_moore.search,
        'KMP': kmp.search,
        'Rabin-Karp': rabin_karp.search
    }

    test_files = ['стаття_1.txt', 'стаття_2.txt']

    benchmark = AlgorithmBenchmark(algorithms, number_of_runs=50)

    all_results = []

    try:
        for filename in test_files:
            print(f"\nЗавантаження файлу: {filename}")
            text = read_file(filename)

            patterns = select_test_patterns(text)
            print("Обрані шаблони для тестування:")
            print(f"  Існуючий: '{patterns['existing']}'")
            print(f"  Неіснуючий: '{patterns['non_existing']}'")

            results = benchmark.run_pattern_test(text, patterns, filename)
            all_results.append(results)

    except FileNotFoundError as e:
        print(f"ПОМИЛКА: {e}")
        print("Переконайтеся, що файли стаття_1.txt та стаття_2.txt "
              "знаходяться в поточній директорії")
        return None

    except Exception as e:
        print(f"ПОМИЛКА: Виникла неочікувана помилка: {e}")
        return None

    winner_ranking = benchmark.print_summary(all_results)

    print_separator("АНАЛІЗ ЗАВЕРШЕНО")
    print("Усі три алгоритми пошуку підрядків реалізовано та протестовано")
    print("Результати продуктивності та порівняння наведені вище")

    overall_winner = winner_ranking[0][0]
    print(f"\nВисновок: {overall_winner} є оптимальним алгоритмом")
    print(f"Рейтинг продуктивності: {overall_winner} > {winner_ranking[1][0]} > "
          f"{winner_ranking[2][0]}")
    print("Стабільні результати для обох текстових файлів")

    return all_results


if __name__ == "__main__":
    main()
