function y = INSERTION_SORT_B(x)
n = length(x);
a = x(1)
for j = 2 : n
    temp=x(j);
    i = BINARY_SEARCH(a, temp);
    b = a(1:i-1);
    c = a(i:end);
    a = [b temp c];
end
y = a;
end

function z = BINARY_SEARCH(arr, val)
L = 0;
R  = length(arr) + 1;
while R ~= L+1
    mid = floor((L+R)/2);
    if arr(mid) <= val
        L = mid;
    else
        R = mid;
    end
end
z = R;
end
