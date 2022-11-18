import random
from typing import Optional

M = 10000000

class Party:
    def __init__(self, salary: int):
        self._salary = salary
        self._x: Optional[int] = None

    def initialize(self) -> int:
        self._x = random.randint(0, M - 1)

        return self._salary + self._x

    def add_salary(self, salaries_sum: int) -> int:
        return self._salary + salaries_sum

    def finalize(self, salaries_sum: int) -> int:
        return salaries_sum - self._x

    def __repr__(self) -> str:
        return f'Party(salary: {self._salary})'

if __name__ == '__main__':
    parties = [Party(random.randint(10000, 100000)) for _ in range(5)]

    print('Party 1 starts the protocol and sends `salaries_sum` to Party 2 using secure channel.')
    salaries_sum = parties[0].initialize()

    for party in parties[1:]:
        print('Party updates and sends `salaries_sum` to next Party using secure channel.')
        salaries_sum = party.add_salary(salaries_sum)

    print('Party 1 computes the `salaries_sum` by substracting random number that was added during initialization.')
    salaries_sum = parties[0].finalize(salaries_sum)

    print(parties)
    print(f'Sum of salaries is: {salaries_sum}.')