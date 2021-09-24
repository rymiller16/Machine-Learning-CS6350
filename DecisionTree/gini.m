function stuff = gini(p,n)
    a = p+n;
    p1 = n/a;
    p2 = p/a;
    stuff = 1-(p1^2)-(p2^2);
end 