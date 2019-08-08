while True:
    sumPrice=0
    print('İstifadəçidən kateqoriyasının kodu:')
    category=input()
    if category!='b'and category!='d' and category!='w':
        continue
    else :    
        print('Sayğacın ilkin göstəricisini qeyd edin:')
        initialIndicator=int(input())
        print('Sayğacın son göstəricisini qeyd edin:')
        lastIndicator=int(input())
        print('Günlərin sayını daxil edin:')
        dayCount=int(input())
        result=lastIndicator-initialIndicator
        print(dayCount)
        if category=='b':
            sumPrice=dayCount*40+0.25*(lastIndicator-initialIndicator)
            
        elif category=='d':
            if lastIndicator-initialIndicator>100:
                sumPrice+=dayCount*60+0.25*(lastIndicator-initialIndicator)
            else:
                sumPrice+=dayCount*60
        elif category=='w':
            sumPrice+=190
            if result>900 and result<=1500:
                sumPrice+=100
            elif result>1500:
                sumPrice+=200+(result-1500)*0.25
    print(sumPrice)

        
       
      
