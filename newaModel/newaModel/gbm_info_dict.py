pest_status_management = { 
'pest_name': "Grape Berry Moth",
'biofix_phenology' : "Wild Grape Bloom",
'biofix_abbrev': 'gbm',
'basetemp': 47.14,

'pre_biofix': {
0: { 'ddlo':  0, 'ddhi':  91,  'altref': ["Pre_0"],
							   'stage': "Dormant", 
                               'status': "Dormant season. No grape berry moth activity at this time.", 
                               'management': "No control methods are recommended at this time as damage comes from direct feeding on developing berries.                                                                                                                                      Vineyards should be classified for risk of grape berry moth damage using the <a href='http://nysipm.cornell.edu/publications/grapeman/files/risk.pdf' target='_blank'>Grape Berry Moth Risk Assessment</a> protocol." },
1: { 'ddlo': 92, 'ddhi': 182,  'altref': ["Pre_1"],
							   'stage': "No activity", 
                               'status': "No grape berry moth activity at this time.  Historically, Concord budbreak in the Lake Erie Region occurs at 133 GDD.",
                               'management': "Ready spray equipment for the growing season." },
2: { 'ddlo':183, 'ddhi':450,  'altref': ["Pre_2"],
							   'stage': "Beginning flight", 
                               'status': "Wild grape bloom often coincides with peak trap catch of the overwintering generation, at 350-400 GDD.",
                               'management': "At this time monitor vineyard edges for evidence of wild grape bloom and enter this date above. Wild grape bloom typically occurs 7-10 days before Concord bloom. The best estimate of biofix (start) of the Grape Berry Moth Degree Day Model is wild grape bloom (50% of blossoms open). Enter this date to initiate model." }},
'post_biofix': {
0: { 'ddlo':   0, 'ddhi': 352, 'altref': ["Post_0"],
							   'stage': "First generation hatching and feeding",
                               'status': "First generation of grape berry moth larvae are hatching and beginning feeding. Grape berry moth will not be at significant population levels in all but the highest risk vineyards.",
                               'management': "Research has shown that this insecticide timing for the first generation provides little, if any, additional control of grape berry moth in vineyards classified as being at low, intermediate or high risk for grape berry moth damage. However, an insecticide timed with the immediate postbloom fungicide application can be used in vineyards experiencing significant crop loss from grape berry moth on a yearly basis or in high value vinifera blocks." },
1: { 'ddlo': 353, 'ddhi': 650, 'altref': ["Post_1"],
							   'stage': "Pupation begins",
                               'status': "Feeding by first generation will cease and pupation will begin when approximately 500 DD have accumulated after wild grape bloom.",
                               'management': "The time for treatment of first generation grape berry moth is over." },
2: { 'ddlo': 651, 'ddhi': 750, 'altref': ["Post_2"],
							   'stage': "First generation flight",
                               'status': "Start of flight of first generation grape berry moth is expected at this time.",
                               'management': "Prepare to scout low and intermediate risk vineyards for grape berry moth damage when DD accumulation after wild grape bloom reaches 750-800 DD. During scouting, determine if damage from first generation larvae exceeds the treatment threshold of 6% damaged clusters. If above threshold, control measures should be applied at 810 DD." },
3: { 'ddlo': 751, 'ddhi': 810, 'altref': ["Post_3"],
							   'stage': "Second generation peak egg-laying",
                               'status': "Females are active and egg-laying is at its peak.",
                               'management': "Control measures should be timed to coincide with 810 DD in high risk vineyards. For materials that must be ingested, e.g. Intrepid, Altacor, it is important to get materials on as close to 810 DD as possible. For low and intermediate risk vineyards, scout between 750-800 DD for damage and apply control measures, timed to coincide with 810 DD, if more than 6% damaged clusters are found." },
4: { 'ddlo': 811, 'ddhi': 900, 'altref': ["Post_4"],
							   'stage': "Second generation egg-laying continues",
                               'status': "Egg-laying continues.",
                               'management': "For materials that are contact insecticides, e.g. pyrethroids and carbamates, apply between 811 and 900 DD." },
5: { 'ddlo': 901, 'ddhi':1550, 'altref': ["Post_5"],
							   'stage': "Second generation larvae completing development",
                               'status': "Second generation larvae are protected within berries and completing their development.",
                               'management': "The most effective time for treatment of second generation grape berry moth is over.  Prepare to scout all vineyard blocks for grape berry moth damage when DD accumulation reaches 1470-1620 DD. During scouting, determine if the number of damaged clusters from previous generation exceeds the treatment threshold of 15%. If above threshold, control measures should be applied starting at 1620 DD." },
6: { 'ddlo':1551, 'ddhi':1620, 'altref': ["Post_6"],
							   'stage': "Third generation peak egg-laying",
                               'status': "Females are active and egg-laying is at its peak.",
                               'management': "Control measures should be timed to coincide with 1620 DD in high risk vineyards. For materials that must be ingested, e.g. Intrepid, Altacor, it is important to get insecticides on as close to 1620 DD as possible. " },
7: { 'ddlo':1621, 'ddhi':1710, 'altref': ["Post_7"],
							   'stage': "Third generation egg-laying continues",
                               'status': "Egg-laying continues.",
                               'management': "For materials that are contact insecticides, e.g. pyrethroids and carbamates, apply between 1621-1710 DD in vineyards where scouting found more than 15% damaged clusters. Low risk vineyards rarely require this treatment." },
8: { 'ddlo':1711, 'ddhi':1800, 'altref': ["Post_8"],
							   'stage': "Third generation larvae completing development",
                               'status': "Third generation larvae are protected within berries and completing their development.",
                               'management': "The most effective time for treatment of second generation grape berry moth is over.  With the exception of extremely warm years, egg-laying is reduced and most pupae enter diapause (overwintering stage) after 1700 DD." },
9: { 'ddlo':1801, 'ddhi':9999, 'altref': ["Post_9"],
							   'stage': "Reduced egg-laying",
                               'status': "Reduced egg-laying after this time, most pupae enter diapause (ovewintering stage) after 1700 DD.",
                               'management': "With the exception of extremely warm years no further action is required." } } }