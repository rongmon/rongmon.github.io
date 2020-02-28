def project_score(MT1=100.,MT2=100.,MT3=100.,Final=100.,HW=100.,EC=100.,PSS=100.,Participation=100.,attendance=100.):
    Weight_PSS=0.1
    Weight_MT=0.15
    Weight_Final=0.3
    Weight_HW=0.1
    Weight_HW=0.1
    EC=EC*0.3
    
    HW_Full= (HW + EC)
    if HW_Full >100.:
        HW_Full=100.
    
    
    
    Class_Participation= Participation* .03
    attendance = attendance*.02
    
    projected_final = (PSS *Weight_PSS) + (HW_Full*Weight_HW) + (MT1*Weight_MT) + (MT3*Weight_MT) +(MT2*Weight_MT)+ (Final*Weight_Final) + Class_Participation + attendance
    
    #Assign letter grade
    grades=['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','D-','F']
    cutoff=[110.,96.67,93.34,90.00,86.67,83.34,80.00,76.67,73.34,70.00,66.67,63.34,60.00,00.]
    letter_grade='NA'
    for i in range(0,len(grades)):
        if ((projected_final < cutoff[i]) & (projected_final >= cutoff[i+1])):
            letter_grade = grades[i]
            
            
    print('-----------------------------------------------------------------')
    print('Percentage='+str(projected_final)+', Letter Grade= '+letter_grade)
