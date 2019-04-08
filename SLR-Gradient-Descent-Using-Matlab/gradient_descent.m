function [updated_theta, history] = gradient_descent(theta,x,y,alpha,iterations)
m = length(y);
history = zeros(iterations,1);

for i = 1: iterations
difference = (x*theta) - y;
temp0 = theta(1) -  (alpha/m)*sum(difference.*x(:,1) );
temp1 = theta(2) -  (alpha/m)*sum(difference.*x(:,2));
updated_theta = [temp0;temp1];
 history(i) = calculate_cost(updated_theta,x,y);
end

end
