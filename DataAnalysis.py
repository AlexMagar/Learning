from matplotlib import pyplot as plt 

# 1.get content from the file life.txt and add into life[] list
def people_life():
    for a in file_life:
        men_life = a.split(',') #split content by ',' and store to men_life
        col=[]
        col.append(men_life[0]) #store 1st item of the list

        # iterate through the list men_life
        # start from 1 to lenght of list to get the value not the country name
        for b in range(1,len(men_life)):
            col.append((float(men_life[b]))) #convert iteam (string) of list into float
        life.append(col) #store to life list

    return life #return list life

# 1.get content from the file bmi_men.csv and add into bmi_men : {} dictionary
def bmi_men_data():
    for a in file_bmi_men:
        men_bmi = a.split(',')
        country = men_bmi[0] #store country name in a list
        col = []
        for b in range(1,len(men_bmi)):
            col.append((float(men_bmi[b])))
        # put the value in the dictionary with country name and associated data    
        bmi_men[country] = col 
    return bmi_men

# 1. get content from the file bmi_women.csv and add into bmi_women : {} dictionary
def bmi_women_data():
    for a in file_bmi_women:
        women_bmi = a.split(',')
        country = women_bmi[0]
        col = []
        for b in range(1,len(women_bmi)):
            col.append((float(women_bmi[b])))
        bmi_women[country] = col
    return bmi_women

# 2. return average value of both BMI men and women and place into "bmi_all" dictionary
def netural_BMI():
    bmi_all = dict()
    men = bmi_men_data() #men dictionary 
    women = bmi_women_data() #women dictionary 

    for key in men:
        d = []
        if key in women:
            # m is a list, contain value of men[key] dictionary
            m = men[key] 
            n = women[key]
            for x in range(len(m)):
                # add men and women list and divide by 2 to get average
                d.append((m[x] + n[x])/2)
                bmi_all[key] = d
    return bmi_all


# 3. calculate minimum, maximum, and median of men and women
def wordwide_statistics():
    avg = netural_BMI() #all value of BMI
    mun = []    #empty list
    print('--- Step 3 ---')
    try:        
        year = int(input('Select a year to find statistics (1980 to 2008): '))
        # check date in range or not
        if year >= 1980 or year <= 2008:
            if year in date_value:
                index = date_value[year] #get the index of date
                #iterate through dictionary
                for key in avg:
                    a = []  #empty list to store list of each dictionary
                    a = avg[key] # sort list of dictionary for median
                    mun.append(a[index])
                    mun = sorted(mun)
                    if len(mun) % 2 != 0:
                        middle_index = int((len(mun) - 1)/2) # middle of the list
                        median = mun[middle_index]
                   # elif len(mun) % 2 == 0:
                   #     middle_index_1 = int(len(mun)/2)
                   #     middle_index_2 = int(len(mun)/2) -1
                   #     median = (mun[middle_index_1] + mun[middle_index_2])/2

                # formatting for 3 decimal precision
                print('Median BMI value in {} was {:.3f}'.format(year,median))
    except :
        print('<Error> That is an invalid year.')

# 4. latest 5-year BMI data for men against women for the three 
# most populous countries in the world (China, India, United States).        
def latest_BMI():
    print('\n--- Step 4 ---')
    print('Men vs women BMI in highest population countries:\n')

    bmi_mens = bmi_men_data() #BMI data for men
    bmi_womens = bmi_women_data() #BMI data for women

    China_last_five_year_men_bmi_total = sum(bmi_mens['China'][24:len(bmi_mens)]) #sum of list
    China_last_five_year_wommen_bmi_total = sum(bmi_womens['China'][24:len(bmi_womens)])
    china_avg_men_bmi = China_last_five_year_men_bmi_total / 5  #average of list
    china_avg_women_bmi = China_last_five_year_wommen_bmi_total / 5

    diff_china = china_avg_women_bmi - china_avg_men_bmi
    avg_china = (china_avg_men_bmi + china_avg_women_bmi) / 2
    percent_diff_china = (diff_china / avg_china) * 100 #percentage difference

    India_last_five_year_men_bmi_total = sum(bmi_mens['India'][24:len(bmi_mens)])
    India_last_five_year_wommen_bmi_total = sum(bmi_womens['India'][24:len(bmi_womens)])
    india_avg_men_bmi = India_last_five_year_men_bmi_total / 5
    india_avg_women_bmi = India_last_five_year_wommen_bmi_total / 5

    diff_india = india_avg_women_bmi - india_avg_men_bmi
    avg_india = (india_avg_men_bmi + india_avg_women_bmi) / 2
    percent_diff_india = (diff_india / avg_india) * 100

    US_last_five_year_men_bmi_total = sum(bmi_mens['United States'][24:len(bmi_mens)])
    US_last_five_year_wommen_bmi_toal = sum(bmi_womens['United States'][24:len(bmi_womens)])
    us_avg_men_bmi = US_last_five_year_men_bmi_total / 5
    us_avg_women_bmi = US_last_five_year_wommen_bmi_toal / 5

    diff_us = us_avg_men_bmi - us_avg_women_bmi
    avg_us = (us_avg_men_bmi + us_avg_women_bmi) / 2
    percent_diff_us = (diff_us / avg_us) * 100
    
    print('*** China ***')
    print('Men:\t{:.2f}'.format(china_avg_men_bmi))
    print('Women:\t{:.2f}'.format(china_avg_women_bmi))
    print('Percentage difference: {:.2f}%'.format(percent_diff_china))

    print('\n*** India ***')
    print('Men:\t{:.2f}'.format(india_avg_men_bmi))
    print('Women:\t{:.2f}'.format(india_avg_women_bmi))
    print('Percentage difference: {:.2f}%'.format(percent_diff_india))

    print('\n*** United States ***')
    print('Men:\t{:.2f}'.format(us_avg_men_bmi))
    print('Women:\t{:.2f}'.format(us_avg_women_bmi))
    print('Percentage difference: {:.2f}%'.format(percent_diff_us))


# 5. plot life expectancy trend of a user selected country
def lifeExpectancy():
    life_expt = people_life()
    avg_bmi = netural_BMI()
    print('\n--- Step 5 ---')
    life_dict_data = dict()
    ctry_list = [] #list of all country
    year_list = []  #list if all year

    # make a dictionary from 2 D list
    for a in range(1,len(life_expt)):
        country_list= life_expt[a][0] 
        ctry_list.append(life_expt[a][0]) #get all country name from the list   
        year = []
        for b in range(1,len(life_expt[0])):
            year.append(life_expt[a][b])
        life_dict_data[country_list] = year

    #list of year
    for a in range(1,len(life_expt[0])):
        year_list.append(int(life_expt[0][a]))
    
    try:        
        country_name =input('Enter the country to visualize life expectancy data: ')
        country_name = country_name.title() #converting first letter of each word in upper case

        if country_name in life_dict_data:

            # get life list that is associated with user input country
            contry_life_data = life_dict_data[country_name]

            # get bmi list that is associated with user input country
            country_BMI_data = avg_bmi[country_name]

            print("Plot for '{}' opens in a new window.".format(country_name))

            #begin plotting
            plt.style.use('seaborn')
            fig = plt.figure()
            ax1 = fig.add_subplot()
            ax1.set_xlabel('year(1980-2008)')
            # 'b*-'  b = blue, * = marker, - = linestyle
            ax1.plot(year_list, contry_life_data,'b*-', label="life expectancy")
            # format axis
            ax1.tick_params(axis='y', labelcolor='b')
            ax1.set_ylabel('Life Expectancy', color='b')
            
            #step 6
            print('\n--- Step 6 ---')
            print('Correlation plot opens in a new window.')
            
            ax2 = ax1.twinx() #create a second axes that shares the same x-axis
            ax2.plot(year_list, country_BMI_data, 'go-', label="BMI")
            ax2.tick_params(axis='y', labelcolor='g')         
            ax2.set_ylabel('BMI average (Men & Women)', color='g')   

            plt.title("BMI vs Life Expectancy")
            fig.legend()
            plt.tight_layout() #padding for plot
        #    plt.grid(True)
            plt.show()

        else:
            print("<error>'{}' is not a valid country.".format(country_name))

    except:
        pass
        print("<error>'{}' is not a valid country.".format(country_name))
                
# main function
if __name__=="__main__":

    # date and indexing
    date_value = {
        1980:0,
        1981:1,
        1982:2,
        1983:3,
        1984:4,
        1985:5,
        1986:6,
        1987:7,
        1988:8,
        1989:9,
        1990:10,
        1991:11,
        1992:12,
        1993:13,
        1994:14,
        1995:15,
        1996:16,
        1997:17,
        1998:18,
        1999:19,
        2000:20,
        2001:21,
        2002:22,
        2003:23,
        2004:24,
        2005:25,
        2006:26,
        2007:27,
        2008:28
    }

    # initiate dictionary and list
    bmi_men = dict()
    bmi_women = dict()
    life = []

    try:
        # open all three file in read mode
        file_bmi_men = open('bmi_men.csv','r')
        file_bmi_women = open('bmi_women.csv','r')
        file_life = open('life.csv','r')

        print('\nA simple data analysis program\n')

        pf = people_life()
        bm = bmi_men_data()
        bw = bmi_women_data()
        bn = netural_BMI()

        if pf and bm and bw and bn != 0:    
            print('--- Step 1 ---')
            print('All dataset has been read into memory.\n')
            print('--- Step 2 ---')
            print('Gender-average BMI data stored in a new dictionary.\n')

        wordwide_statistics()

        latest_BMI()

        lifeExpectancy()

    except FileNotFoundError:
        print('<Error> File not found')

    else:
        print('\nGoodbye.\n')


