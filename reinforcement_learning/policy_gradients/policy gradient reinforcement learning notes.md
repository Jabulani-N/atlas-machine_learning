notes from [how policy gradient reinforcement learning works](https://www.youtube.com/watch?v=A_2U6Sx67sE) video

use deep neural network to approx the policy
- **uses softmax activation funciton**

uses backpropagation after each episode for updates of 

backpropagation to update weights of deep neural network:
* use discounted future returns as weights
* use actoin as label


eventually we get to where we'll the g_t gradient in policy space  