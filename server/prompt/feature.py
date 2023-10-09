
generate_feature_pmt ='''

Let's play a life simulated game. 
First, we need to generate the player's features. 

Requirements:
- Please provide 7 features to choose from.
- positive features are more than negtive features.
- Features should be detailed, not general.
- Please privide feature related with {style} 

Return
<res>
[
	{{"feature_name": "feature_description"}},
	{{"feature_name": "feature_description"}},
	{{"feature_name": "feature_description"}},
	....
]
</res>





'''

generate_feature_exeample = [
{ "Brain Implantation": "Implant computer chips into the brain to acquire powerful computational and memory abilities." },
{ "Genetic Modification": "Modify DNA to achieve exceptional physical fitness and the chance of immortality." },
{ "Mechanical Modification": "Replace some limbs with mechanical prosthetics to enhance combat power." },
{ "Hacking Skills": "Master all sorts of computer and network knowledge, capable of cracking passwords and hacking into various systems." },
{ "Slum Survival": "Grew up in a slum, accustomed to harsh environments but a survival skill expert." },
{ "Drug Addiction": "Apply new drugs produced by future technology, achieving temporary to permanent ability enhancement." },
{ "Life on the Run": "Constantly evading pursuit due to various reasons, leading a displaced life." },
{ "Black Market Trading": "Acquire various goods and resources through illegal channels." },
]





{ "脑植入": "将计算机芯片植入大脑,获取强大的运算与记忆能力。" },
{ "基因改造": "改造DNA,获得超常体质与长生不老的机会。"},
{ "机械改造": "替换部分肢体为机械义肢,获得强化战斗力。" },
{ "黑客技能": "精通各式电脑与网络知识,能破解帐号密码和黑入各类系统。" },
{ "贫民窟生存": "在贫民窟长大,习惯艰难环境但生存技巧达人。" },
{ "毒瘾": "应用未来科技产生的新型药物,获得短暂至永久的能力提升。" },       
{ "逃亡生活": "因种种原因而不断逃避追捕,过着流离失所的生活。"},
{ "黑市交易": "通过非法渠道取得各种商品与资源。" },