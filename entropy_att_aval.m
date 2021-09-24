function stuff = entropy_att_aval(attribute_aval,data)
    
    global depth;
    %taking count of all data 
    %count 1 = unacc, count2 = acc, count3 = good, count4 = vgood
    count1 = 0; count2 = 0; count3 = 0; count4 = 0;
    n1 = 0;n2=0;n3=0;n4=0;n5=0;n6=0;n7=0;n8=0;n9=0;n10=0;n11=0;n12=0;n13=0;n14=0;n15=0;n16=0;
    width = size((data),2);
    
    for i=1:length(data)
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
    total_n = count1+count2+count3+count4; 

    %count 1 = unacc, count2 = acc, count3 = good, count4 = vgood
    count1 = 0; count2 = 0; count3 = 0; count4 = 0; counter = 0;
    width = size((data),2);
    
    if attribute_aval == "buying"
        counter = 1;
    elseif attribute_aval == "maint"
        counter = 2;
    elseif attribute_aval == "doors"
        counter = 3;  
    elseif attribute_aval == "persons"
        counter = 4;
    elseif attribute_aval == "lug_boot"
        counter = 5;
    elseif attribute_aval == "safety"
        counter = 6;
    end
      
    if counter == 1 || counter == 2 
        for i=1:length(data)
            if (data{i,counter,depth} == "vhigh")
                if (data{i,width,depth} == "unacc")
                    n1 = n1+1;
                elseif (data{i,width,depth} == "acc")
                    n2 = n2+1;
                elseif (data{i,width,depth} == "good")
                    n3 = n3+1;
                elseif (data{i,width,depth} == "vgood")
                    n4 = n4+1;
                end 
            elseif (data{i,counter,depth} == "high")
                if (data{i,width,depth} == "unacc")
                    n5 = n5+1;
                elseif (data{i,width,depth} == "acc")
                    n6 = n6+1;
                elseif (data{i,width,depth} == "good")
                    n7 = n7+1;
                elseif (data{i,width,depth} == "vgood")
                    n8 = n8+1;
                end 
            elseif (data{i,counter,depth} == "med")
                if (data{i,width,depth} == "unacc")
                    n9 = n9+1;
                elseif (data{i,width,depth} == "acc")
                    n10 = n10+1;
                elseif (data{i,width,depth} == "good")
                    n11 = n11+1;
                elseif (data{i,width,depth} == "vgood")
                    n12 = n12+1;
                end 
            elseif (data{i,counter,depth} == "low")
                if (data{i,width,depth} == "unacc")
                    n13 = n13+1;
                elseif (data{i,width,depth} == "acc")
                    n14 = n14+1;
                elseif (data{i,width,depth} == "good")
                    n15 = n15+1;
                elseif (data{i,width,depth} == "vgood")
                    n16 = n16+1;
                end 
            end 
        end 
    elseif counter == 3
        for i=1:length(data)
            if (data{i,counter,depth} == "2")
                if (data{i,width,depth} == "unacc")
                    n1 = n1+1;
                elseif (data{i,width,depth} == "acc")
                    n2 = n2+1;
                elseif (data{i,width,depth} == "good")
                    n3 = n3+1;
                elseif (data{i,width,depth} == "vgood")
                    n4 = n4+1;
                end 
            elseif (data{i,counter,depth} == "3")
                if (data{i,width,depth} == "unacc")
                    n5 = n5+1;
                elseif (data{i,width,depth} == "acc")
                    n6 = n6+1;
                elseif (data{i,width,depth} == "good")
                    n7 = n7+1;
                elseif (data{i,width,depth} == "vgood")
                    n8 = n8+1;
                end 
            elseif (data{i,counter,depth} == "4")
                if (data{i,width,depth} == "unacc")
                    n9 = n9+1;
                elseif (data{i,width,depth} == "acc")
                    n10 = n10+1;
                elseif (data{i,width,depth} == "good")
                    n11 = n11+1;
                elseif (data{i,width,depth} == "vgood")
                    n12 = n12+1;
                end 
            elseif (data{i,counter,depth} == "5more")
                if (data{i,width,depth} == "unacc")
                    n13 = n13+1;
                elseif (data{i,width,depth} == "acc")
                    n14 = n14+1;
                elseif (data{i,width,depth} == "good")
                    n15 = n15+1;
                elseif (data{i,width,depth} == "vgood")
                    n16 = n16+1;
                end 
            end 
        end
    elseif counter == 4
        for i=1:length(data)
            if (data{i,counter,depth} == "2")
                if (data{i,width,depth} == "unacc")
                    n1 = n1+1;
                elseif (data{i,width,depth} == "acc")
                    n2 = n2+1;
                elseif (data{i,width,depth} == "good")
                    n3 = n3+1;
                elseif (data{i,width,depth} == "vgood")
                    n4 = n16+1;
                end 
            elseif (data{i,counter,depth} == "4")
                if (data{i,width,depth} == "unacc")
                    n5 = n4+1;
                elseif (data{i,width,depth} == "acc")
                    n6 = n5+1;
                elseif (data{i,width,depth} == "good")
                    n7 = n6+1;
                elseif (data{i,width,depth} == "vgood")
                    n8 = n16+1;
                end 
            elseif (data{i,counter,depth} == "more")
                if (data{i,width,depth} == "unacc")
                    n9 = n7+1;
                elseif (data{i,width,depth} == "acc")
                    n10 = n8+1;
                elseif (data{i,width,depth} == "good")
                    n11 = n9+1;
                elseif (data{i,width,depth} == "vgood")
                    n12 = n12+1;
                end 
            end 
        end
    elseif counter == 5
        for i=1:length(data)
            if (data{i,counter,depth} == "small")
                if (data{i,width,depth} == "unacc")
                    n1 = n1+1;
                elseif (data{i,width,depth} == "acc")
                    n2 = n2+1;
                elseif (data{i,width,depth} == "good")
                    n3 = n3+1;
                elseif (data{i,width,depth} == "vgood")
                    n4 = n16+1;
                end 
            elseif (data{i,counter,depth} == "med")
                if (data{i,width,depth} == "unacc")
                    n5 = n4+1;
                elseif (data{i,width,depth} == "acc")
                    n6 = n5+1;
                elseif (data{i,width,depth} == "good")
                    n7 = n6+1;
                elseif (data{i,width,depth} == "vgood")
                    n8 = n16+1;
                end 
            elseif (data{i,counter,depth} == "big")
                if (data{i,width,depth} == "unacc")
                    n9 = n7+1;
                elseif (data{i,width,depth} == "acc")
                    n10 = n8+1;
                elseif (data{i,width,depth} == "good")
                    n11 = n9+1;
                elseif (data{i,width,depth} == "vgood")
                    n12 = n16+1;
                end 
            end 
        end
    elseif counter == 6
        for i=1:length(data)
            if (data{i,counter,depth} == "low")
                if (data{i,width,depth} == "unacc")
                    n1 = n1+1;
                elseif (data{i,width,depth} == "acc")
                    n2 = n2+1;
                elseif (data{i,width,depth} == "good")
                    n3 = n3+1;
                elseif (data{i,width,depth} == "vgood")
                    n4 = n16+1;
                end 
            elseif (data{i,counter,depth} == "med")
                if (data{i,width,depth} == "unacc")
                    n5 = n4+1;
                elseif (data{i,width,depth} == "acc")
                    n6 = n5+1;
                elseif (data{i,width,depth} == "good")
                    n7 = n6+1;
                elseif (data{i,width,depth} == "vgood")
                    n8 = n16+1;
                end 
            elseif (data{i,counter,depth} == "high")
                if (data{i,width,depth} == "unacc")
                    n9 = n7+1;
                elseif (data{i,width,depth} == "acc")
                    n10 = n8+1;
                elseif (data{i,width,depth} == "good")
                    n11 = n9+1;
                elseif (data{i,width,depth} == "vgood")
                    n12 = n16+1;
                end 
            end 
        end
    end 
    
    if counter == 1 || counter == 2 || counter == 3
        part1 = entropy_by4(n1,n2,n3,n4);
        total1 = n1+n2+n3+n4;
        part2 = entropy_by4(n5,n6,n7,n8);
        total2 = n5+n6+n7+n8;
        part3 = entropy_by4(n9,n10,n11,n12);
        total3 = n9+n10+n11+n12;
        part4 = entropy_by4(n13,n14,n15,n16);
        total4 = n13+n14+n15+n16;
        inf_entropy = (total1/total_n)*part1 + (total2/total_n)*part2 + (total3/total_n)*part3 + (total4/total_n)*part4;
    elseif counter == 4 || counter == 5 || counter == 6
        part1 = entropy_by4(n1,n2,n3,n4);
        total1 = n1+n2+n3+n4;
        part2 = entropy_by4(n5,n6,n7,n8);
        total2 = n5+n6+n7+n8;
        part3 = entropy_by4(n9,n10,n11,n12);
        total3 = n9+n10+n11+n12;
        inf_entropy = (total1/total_n)*part1 + (total2/total_n)*part2 + (total3/total_n)*part3;
    end

    stuff = inf_entropy;
end 
