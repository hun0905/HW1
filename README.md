# hw1
1.Download the main.py and 108061217.csv in the hw1 ($git clone https://github.com/hun0905/hw1.git)
<br>2.Run the code by  $python3 main.py
3.the terminal should output [['C0A880', 1.2], ['C0F9A0', 1.8], ['C0G640', 3.7], ['C0R190', 2.1], ['C0X260', 3.7]]
In the code, first I remove the data whose WDSD values is '-99.000' or '-999.000'
Then I get the maximum range of C0A880, C0F9A0, C0G640, C0R190, C0X26
Finally, output the  ID of the station and the maximum range of it in the lexicographical order. 
The result I get:  [['C0A880', 1.2], ['C0F9A0', 1.8], ['C0G640', 3.7], ['C0R190', 2.1], ['C0X260', 3.7]]
