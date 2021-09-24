%for homework 1

prompt = 'P: ';
p = input(prompt);

prompt2 = 'N: ';
n = input(prompt2);

total = p+n;
if p == 0 
    stuff1 = 0;
else 
    stuff1 = (-p/total)*log2(p/total);
end 
    
if n == 0
    stuff2 = 0;
else 
    stuff2 = (n/total)*log2(n/total);
end 

entropy = stuff1 - stuff2
