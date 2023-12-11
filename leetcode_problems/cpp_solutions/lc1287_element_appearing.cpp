#include <iostream>
#include <vector>
using std::vector;

class Solution
{
public:
    int fisrtOccurence(vector<int> &array, int target)
    {
        int start = 0;
        int end = array.size() - 1;

        while (start < end)
        {
            int mid = start + (end - start) / 2;
            if (array[mid] < target)
            {
                start = mid + 1;
            }
            else
            {
                end = mid;
            }
        }

        return end;
    }

public:
    int findSpecialInteger(vector<int> &array)
    {
        int size = array.size();
        if (size == 1)
        {
            return array[0];
        }

        vector<int> quarters = {
            array[size / 4],
            array[size / 2],
            array[size * 3 / 4],
        };

        for (int &quartedNum : quarters)
        {
            int position = fisrtOccurence(array, quartedNum);
            if (array[position + size / 4] == quartedNum)
            {
                return quartedNum;
            }
        }

        return -1;
    }
};

int main()
{
    vector<int> array = {1,
                         2,
                         2,
                         6,
                         6,
                         6,
                         6,
                         7,
                         10};

    Solution sol = Solution();
    int output = sol.findSpecialInteger(array);

    std::cout << output << std::endl;

    return 0;
}