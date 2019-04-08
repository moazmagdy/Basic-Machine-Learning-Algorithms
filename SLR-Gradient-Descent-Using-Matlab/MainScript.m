% Main Script
% Start by Importing training data
data = load('ex1data1.txt');
y = data(:,2);
m = length(y); %Number of training examples
x = [ones(m,1), data(:,1)]; %Assuming that Theta node factor is x = 1
theta = zeros(2,1);  %Initialize thets with zeros in 2 x 1 such that it can be multiplied by X (m x 2)

initial_cost = calculate_cost(theta,x,y); %Compute Initial cost
iterations = 1500;  %The stopping criteria
alpha = 0.005;   % The learning rate

[theta, cost_history] = gradient_descent(theta,x,y,alpha,iterations);

fprintf('The best values for thetas are: \n')
 theta(1),theta(2)
fprintf('The best value for cost function is: \n ')
cost_history(end)