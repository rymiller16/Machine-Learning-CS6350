function stuff = entropy_DS(data)
    
    global depth
    %count 1 = unacc, count2 = acc, count3 = good, count4 = vgood
    count1 = 0; count2 = 0; count3 = 0; count4 = 0;
    
    width = size(data,2);
%     if depth == 1
        length = size(data); 
%     else
%         for i=1:size(data,1)
%             if(data(i,:,depth+1)) == "0"
%                 length = i - 1;
%             elseif i == size(data,1)
%                 length = size(data,1);
%             end 
%         end 
%     end 
    
    for i=1:length
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
    
    entropy = (-count1/total)*log4(count1/total) - (count2/total)*log4(count2/total) - (count3/total)*log4(count3/total) - (count4/total)*log4(count4/total); 
    stuff = entropy;
end 

    
    
    