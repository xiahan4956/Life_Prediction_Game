

predict_pmt = '''

Let's play this life simulation game.


<Return> 
You should return the following JSON:
[
	{{
		event: "a sentence about a current year thing. The thing could be about the player or the environment",
		age:"the player's current age",
	}},
	{{
		event: "a sentence about a current year thing. The thing could be about the player or the environment",
		age:"the player's current age",
	}},
	...
]
</Return>

<History>
There is our past chat content:
{history}
</History>


<Backgrounds> 
the maximum value for each attribute is 10. The player's initial attribute values are:
{atrributes}


The player select features above:
{features}
</Backgrounds>




<Requirements> 
- The prediction should be based on world setting: {style}
- The prediction should be based on the player's attributes.
- The prediction should be based on the player's features.
- The prediction should be matched human age and match world setting: {style}.Do not forget world setting: {style}
- Every prediction has  more  positive things than negative things.
- The prediction could talk about the player or the player's environment
- The prediction should talk about concrete facts, not abstract things.
- The prediction should be avoid duplicated.
- The player should die at the age of {dead_age}.
- Don't die early. You should inform the player of their death exactly.
- Predict the player's life from age {start_age} to {end_age}, year by year.
- Don't skip any year and drop any year when make prediction.
</Requirements>


Now,please predict.
'''

# - Use "You" to refer to the player.
# - Negative events should be more than positive events.