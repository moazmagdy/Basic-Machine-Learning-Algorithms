function J = calculate_cost(theta,x,y)
m = length(y);

J = (1/(2*m)) * sum(((x*theta) - y).^2);
end