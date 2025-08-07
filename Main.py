

```python
# -*- coding: utf-8 -*-

import random
import time
import numpy as np

# =========================================================
# بخش ۱: کلاس پایه برای تعریف مسئلهٔ شما
# =========================================================

class YourProblem:
    def __init__(self):
        # تعریف استراتژی‌های ممکن برای مسئله
        self.strategies = {
            "Strategy_A": self.evaluate_strategy_A,
            "Strategy_B": self.evaluate_strategy_B,
            "Strategy_C": self.evaluate_strategy_C,
        }
        self.problem_name = "My New Challenge"
        
    def evaluate_strategy_A(self):
        # منطق و شبیه‌سازی برای استراتژی A
        # اینجا کد مربوط به راه‌حل خود را قرار دهید
        score = random.uniform(0.1, 0.5)
        return score
    
    def evaluate_strategy_B(self):
        # منطق و شبیه‌سازی برای استراتژی B
        # اینجا کد مربوط به راه‌حل خود را قرار دهید
        score = random.uniform(0.4, 0.9)
        return score

    def evaluate_strategy_C(self):
        # منطق و شبیه‌سازی برای استراتژی C
        # اینجا کد مربوط به راه‌حل خود را قرار دهید
        score = random.uniform(0.2, 0.8)
        return score

# =========================================================
# بخش ۲: هستهٔ فراشناختی (مغز پروژه)
# =========================================================

class TheMetaCognitiveCore:
    def __init__(self, problem):
        self.problem = problem
        self.strategies = list(problem.strategies.keys())
        self.last_best_score = -float('inf')
        self.best_strategy = "None"
        
    def run(self, iterations=10):
        print("🧠 هستهٔ فراشناختی در حال آغاز به کار...")
        print("---")
        
        for i in range(iterations):
            current_strategy_name = random.choice(self.strategies)
            evaluate_func = self.problem.strategies[current_strategy_name]
            
            print(f"\n⛏️ هسته در حال آزمایش فرااستراتژی '{current_strategy_name}' است.")
            
            try:
                current_score = evaluate_func()
                
                if current_score > self.last_best_score:
                    print(f"✅ هسته، فرااستراتژی '{current_strategy_name}' را بهینه یافت. نمرهٔ جدید: {current_score:.4f}")
                    self.last_best_score = current_score
                    self.best_strategy = current_strategy_name
                else:
                    print(f"⚠️ هسته، فرااستراتژی '{current_strategy_name}' را ناکارآمد یافت. نمره: {current_score:.4f}")

            except Exception as e:
                print(f"❌ خطایی در اجرای استراتژی '{current_strategy_name}' رخ داد: {e}")
                
            time.sleep(1)

        print("\n" + "=" * 50)
        print(f"🎯 هسته به بهترین فرااستراتژی خود برای '{self.problem.problem_name}' رسید:")
        print(f"   بهترین فرااستراتژی: {self.best_strategy}")
        print(f"   بهترین نمرهٔ فراشناختی: {self.last_best_score:.4f}")
        print("=" * 50)


# =========================================================
# بخش ۳: حلقه اصلی
# =========================================================

if __name__ == "__main__":
    # مرحله اول: یک مسئلهٔ جدید تعریف کنید
    my_new_problem = YourProblem()
    
    # مرحله دوم: هستهٔ فراشناختی را با مسئلهٔ جدید اجرا کنید
    core = TheMetaCognitiveCore(my_new_problem)
    core.run(iterations=10)
