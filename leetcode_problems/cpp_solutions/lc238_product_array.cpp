#include <iostream>
#include <vector>

class Solution
{
public:
    std::vector<int> run(std::vector<int> &numbers)
    {
        std::vector<int> answers(numbers.size(), 1);

        int current = 1;
        for (int index = 0; index < numbers.size(); index++)
        {
            answers[index] *= current;
            current *= numbers[index];
        }

        current = 1;
        for (int index = numbers.size() - 1; index >= 0; index--)
        {
            answers[index] *= current;
            current *= numbers[index];
        }

        return answers;
    }
};

int main()
{
    std::vector<int> nums = {1, 2, 3, 4};
    Solution sol;

    std::vector<int> asnwers = sol.run(nums);
    for (auto answ : asnwers)
    {
        std::cout << answ << std::endl;
    }

    return 0;
}