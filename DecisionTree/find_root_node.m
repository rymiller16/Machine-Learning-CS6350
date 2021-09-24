function stuff = find_root_node(Attributes,attribute,Label)
    %Attribute = {"buying","maint","doors","persons","lug_boot","safety"};
     
    %buying = low
    %counter_low -> array of 4, %count 1 = unacc, count2 = acc, count3 = good, count4 = vgood
    for i=1:length(Attributes)
        if Attributes(i,1) == "low"
            if Label(i,1) == "unacc"
                counter_low(1,1) = counter_low(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_low(1,2) = counter_low(1,2)+1;
            elseif Label(i,1) == "good"
                counter_low(1,3) = counter_low(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_low(1,4) = counter_low(1,4)+1;
            end 
        elseif Attributes(i,1) == "med"
            if Label(i,1) == "unacc"
                counter_med(1,1) = counter_med(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_med(1,2) = counter_med(1,2)+1;
            elseif Label(i,1) == "good"
                counter_med(1,3) = counter_med(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_med(1,4) = counter_med(1,4)+1;
            end
        elseif Attributes(i,1) == "high"
            if Label(i,1) == "unacc"
                counter_high(1,1) = counter_high(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_high(1,2) = counter_high(1,2)+1;
            elseif Label(i,1) == "good"
                counter_high(1,3) = counter_high(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_high(1,4) = counter_high(1,4)+1;
            end 
        elseif Attributes(i,1) == "vhigh"
            if Label(i,1) == "unacc"
                counter_high(1,1) = counter_high(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_high(1,2) = counter_high(1,2)+1;
            elseif Label(i,1) == "good"
                counter_high(1,3) = counter_high(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_high(1,4) = counter_high(1,4)+1;
            end   
        end 
        
        % now for maint------------
        
        if Attributes(i,1) == "low"
            if Label(i,1) == "unacc"
                counter_low(1,1) = counter_low(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_low(1,2) = counter_low(1,2)+1;
            elseif Label(i,1) == "good"
                counter_low(1,3) = counter_low(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_low(1,4) = counter_low(1,4)+1;
            end 
        elseif Attributes(i,1) == "med"
            if Label(i,1) == "unacc"
                counter_med(1,1) = counter_med(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_med(1,2) = counter_med(1,2)+1;
            elseif Label(i,1) == "good"
                counter_med(1,3) = counter_med(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_med(1,4) = counter_med(1,4)+1;
            end
        elseif Attributes(i,1) == "high"
            if Label(i,1) == "unacc"
                counter_high(1,1) = counter_high(1,1)+1;
            elseif Label(i,1) == "acc"
                counter_high(1,2) = counter_high(1,2)+1;
            elseif Label(i,1) == "good"
                counter_high(1,3) = counter_high(1,3)+1;
            elseif Label(i,4) == "vgood"
                counter_high(1,4) = counter_high(1,4)+1;
            end
    end 
    
    
           
        
end 