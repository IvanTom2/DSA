#include <iostream>
#include <vector>

class Solution
{
public:
    bool run(std::vector<int> &flowerbed, int n)
    {
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);

        int maxlen = flowerbed.size();
        for (int index = 1; index < maxlen - 1 && n > 0; index++)
        {
            if (flowerbed[index] == 0)
            {
                if (flowerbed[index - 1] == 0 && flowerbed[index + 1] == 0)
                {
                    n--;
                    index++;
                }
            }
        }
        return n == 0;
    }
};

int main()
{
    std::vector<int> flowerbed = {1, 0, 1, 0, 1};
    int n = 1;

    Solution sol = Solution();
    bool result = sol.run(flowerbed, n);
    std::cout << result << std::endl;

    return 0;
}