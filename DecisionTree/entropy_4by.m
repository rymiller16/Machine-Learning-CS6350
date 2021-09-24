function stuff = entropy_4by(n1,n2,n3,n4)
    total = n1+n2+n3+n4;
    
    stuff = (-n1/total)*log4(n1/total)-(n2/total)*log4(n2/total)-(n3/total)*log4(n3/total)-(n4/total)*log4(n4/total);
    
end