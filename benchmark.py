import timeit
from utils import format_time, print_separator


class AlgorithmBenchmark:
    def __init__(self, algorithms, number_of_runs=50):
        self.algorithms = algorithms
        self.number_of_runs = number_of_runs

    def measure_single_algorithm(self, algorithm_func, text, pattern):
        def test_function():
            return algorithm_func(text, pattern)

        total_time = timeit.timeit(test_function, number=self.number_of_runs)
        return total_time / self.number_of_runs

    def run_single_test(self, text, pattern, pattern_type=""):
        print(f"\nТестування {pattern_type} шаблону: '{pattern}'")
        print("-" * 60)

        results = {}
        performance_data = []

        print("Результати вимірювань:")
        for algo_name, algo_func in self.algorithms.items():
            avg_time = self.measure_single_algorithm(algo_func, text, pattern)
            result_index = algo_func(text, pattern)  # Get result directly

            results[algo_name] = {
                'time': avg_time,
                'result_index': result_index,
                'found': result_index != -1
            }

            performance_data.append((algo_name, avg_time))
            print(f"{algo_name:12}: {format_time(avg_time)}")

        performance_data.sort(key=lambda x: x[1])
        fastest = performance_data[0]
        print(f"НАЙШВИДШИЙ: {fastest[0]} ({format_time(fastest[1])})")

        return results

    def run_pattern_test(self, text, patterns, filename):
        print_separator(f"ТЕСТУВАННЯ ФАЙЛУ: {filename}")
        print(f"Довжина тексту: {len(text):,} символів")

        print("\nМЕТОДОЛОГІЯ ТЕСТУВАННЯ:")
        print("• Кількість запусків для кожного вимірювання: 50")
        print("• Одиниця виміру: мілісекунди (для зручності порівняння)")
        print("• Тестування двох типів шаблонів: існуючих та неіснуючих")
        print("• Використання модуля timeit для точних вимірювань")

        file_results = {
            'filename': filename,
            'text_length': len(text),
            'patterns': patterns,
            'results': {}
        }

        for pattern_type, pattern in patterns.items():
            results = self.run_single_test(text, pattern, pattern_type)
            if results:
                file_results['results'][pattern_type] = results

        return file_results

    def print_summary(self, all_results):
        print_separator("КОМПЛЕКСНИЙ ПІДСУМОК")

        for file_result in all_results:
            print(f"\nФАЙЛ: {file_result['filename']}")
            print(f"Довжина: {file_result['text_length']:,} символів")

            for pattern_type, pattern_results in file_result['results'].items():
                pattern_name = "Існуючий" if pattern_type == "existing" else "Неіснуючий"
                print(f"\n  {pattern_name} шаблон:")

                sorted_results = sorted(
                    pattern_results.items(),
                    key=lambda x: x[1]['time']
                )

                for i, (algo_name, data) in enumerate(sorted_results):
                    rank = ["1st", "2nd", "3rd"][i]
                    print(f"    {rank} {algo_name}: {format_time(data['time'])}")

        print_separator("ЗАГАЛЬНИЙ РЕЙТИНГ АЛГОРИТМІВ")

        algo_total_times = {name: 0 for name in self.algorithms.keys()}
        algo_test_count = {name: 0 for name in self.algorithms.keys()}

        for file_result in all_results:
            for pattern_results in file_result['results'].values():
                for algo_name, data in pattern_results.items():
                    algo_total_times[algo_name] += data['time']
                    algo_test_count[algo_name] += 1

        overall_averages = {
            algo: algo_total_times[algo] / algo_test_count[algo]
            for algo in self.algorithms.keys()
        }

        sorted_overall = sorted(overall_averages.items(), key=lambda x: x[1])

        print("Середня продуктивність у всіх тестах:")
        for i, (algo_name, avg_time) in enumerate(sorted_overall):
            rank = ["1st", "2nd", "3rd"][i]
            print(f"{rank} {algo_name}: {format_time(avg_time)} (середнє)")

        winner = sorted_overall[0]
        print(f"\nЗАГАЛЬНИЙ ПЕРЕМОЖЕЦЬ: {winner[0]} ({format_time(winner[1])} середнє)")

        print_separator("АНАЛІЗ КОМПРОМІСІВ ТА ОСОБЛИВОСТЕЙ")

        print("\nBoyer-Moore:")
        print("+ Найкраща продуктивність на практичних даних")
        print("+ Ефективний пропуск символів завдяки таблиці зсувів")
        print("- Складність реалізації вища за інші")
        print("- Може бути повільний на коротких шаблонах")

        print("\nKMP (Knuth-Morris-Pratt):")
        print("+ Гарантована лінійна складність O(n+m)")
        print("+ Ніколи не повертається назад у тексті")
        print("- Постійні накладні витрати на LPS таблицю")
        print("- Не завжди оптимальний на практиці")

        print("\nRabin-Karp:")
        print("+ Простота реалізації")
        print("+ Ефективний для пошуку множини шаблонів")
        print("- Залежність від якості хеш-функції")
        print("- Можливі колізії хешів требують додаткової перевірки")

        print(f"\nРЕКОМЕНДАЦІЯ: Використовуйте {winner[0]} для подібних завдань пошуку")

        return sorted_overall

