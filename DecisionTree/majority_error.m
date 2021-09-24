function stuff = majority_error(p,n)
    if(p > n)
        stuff = (n)/(p+n);
    else 
        stuff = (p)/(p+n);
end 