import pandas as p

state = {"Andhra Pradesh": [53903393,27], "Arunachal Pradesh" :[1570458,153], "Assam":[35607039,41],
         "Bihar" :[124799926,12], "Chhattisgarh" :[29436231,48], "Delhi" :[18710922,63], "Goa" :[1586250,153],
         "Gujarat" :[63872399,23], "Haryana" :[28204692,51], "Himachal Pradesh" :[7451955,104], "Jharkhand" :[38593948,37],
         "Karnataka" :[67562686,21], "Kerala" :[35699443,41], "Madhya Pradesh" :[85358965,17], "Maharashtra" :[123144223,12],
         "Manipur" :[3091545,137], "Meghalaya" :[3366710,135], "Mizoram" :[1239244,158], "Nagaland" :[2249695,146],
         "Odisha" :[46356334,31], "Punjab" :[30141373,48], "Rajasthan" :[81032689,20], "Sikkim" :[690251,166],
         "Tamil Nadu" :[77841267,20], "Telegana" :[39362732,36], "Tripura" :[4169794,130], "Uttar Pradesh" :[237882725,5],
         "Uttarakhand" :[11250858,84], "West Bengal" :[99609303,15]}
for state_name, state_details in state.items():
    print(state_name,":",state_details)
statedetail= p.DataFrame.from_dict(state, orient='index')
print(statedetail)
statedetail.to_csv('state')              #storing into csv file

