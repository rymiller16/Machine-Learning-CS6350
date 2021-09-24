function stuff = inf_entropy(part1,part2,part3,part4,data)
    
    %count 1 = unacc, count2 = acc, count3 = good, count4 = vgood
    count1 = 0; count2 = 0; count3 = 0; count4 = 0;
    width = size((data),2);
    global depth;
    
   for i=1:size(data,1)
        if(data(i,:,depth)) == "0"
            length1 = i - 1;
            break;
        elseif i == size(data,1)
            length1 = size(data,1);
        end 
    end 
    
    %added depth here 
    for i=1:length1
        if (data{i,width,depth} == "unacc")
            count1 = count1+1;
        elseif (data{i,width,depth} == "acc")
            count2 = count2+1;
        elseif (data{i,width,depth} == "good")
            count3 = count3+1;
        elseif (data{i,width,depth} == "vgood")
            count4 = count4+1;
        end 
    end 
    total = count1+count2+count3+count4;
    
    stuff = (-n1/total)*log4(n1/total)-(n2/total)*log4(n2/total)-(n3/total)*log4(n3/total)-(n4/total)*log4(n4/total);
    
end