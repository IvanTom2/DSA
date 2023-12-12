#include <vector>
#include <iostream>

class Solution
{
public:
    int run(std::vector<int> &nums)
    {
        int max1 = 0;
        int max2 = 0;

        for (auto num : nums)
        {
            if (num > max2)
            {
                if (num > max1)
                {
                    int temp = max1;
                    max1 = num;
                    max2 = temp;
                }
                else
                {
                    max2 = num;
                }
            }
        }

        return (max1 - 1) * (max2 - 1);
    }
};

int main()
{
    std::vector<int> nums = {2, 4, 5, 1, 3};

    Solution sol;
    int answer = sol.run(nums);

    std::cout << answer << std::endl;

    return 0;
}