function data = return_subtable(data,node,sub_attribute)
    
    global depth;
    count = 0;
    
    sub_attribute = sub_attribute;
    
    if node == "buying"
        count = 1;
    elseif node == "maint"
        count = 2;
    elseif node == "doors"
        count = 3;
    elseif node == "persons"
        count = 4;
    elseif node == "lug_boot"
        count = 5;
    elseif node == "safety"
        count = 6; 
    end 
    
    j=1;
    for i=1:length(data)
        if(data(i,count,depth) == sub_attribute)
            data(j,:,depth+1) = data(i,:,depth);
            j=j+1;
        end 
    end 

k = j;
    while(k<length(data)+1)
        data(k,:,depth+1) = "0";
        k=k+1;
    end 

end 
