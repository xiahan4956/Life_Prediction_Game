<template>
    <h1 class="title">Here is your life</h1>
    <div class="page_container"> 
        <div class="predict_box" v-for="prediction in predictions" :key="prediction.id">
            {{ prediction.text }}
        </div>
        <div v-if="isLoading">Claude is loading...</div>
        <comfirm-button v-if="restartGame" class="main_button" text="Restart" @click="resetGame" />    
    </div>    
</template>

<script>
import ComfirmButton from './ComfirmButton.vue';

    export default {
        name: "PredictLife",
        components: {
            ComfirmButton 
        },
        mounted(){
            this.game_style = localStorage.getItem('game_style');
            this.attributes = JSON.parse(localStorage.getItem('attributes'));
            this.dead_age = localStorage.getItem('dead_age');
            this.features = JSON.parse(localStorage.getItem('selectedFeatures'));

            this.fetchPrediction();
            
        
        },
        data() {
            return {
                game_style: null,
                features: null,
                attributes: null,
                selectedStyle: null,
                dead_age: null,
                predictions: [],
                isLoading: true,
                restartGame: false,
                prediction_history: '',
                start_age:0,    
            };
        },
        methods: {
            async fetchPrediction() {
                try {
                    const response = await this.$http.post('https://qq4956.pythonanywhere.com/api/predict', { 
                        game_style:this.game_style,
                        attributes:this.attributes,
                        features:this.features,
                        dead_age:this.dead_age,
                        start_age:this.start_age,
                        prediction_history: this.prediction_history });
                    const { prediction, continue_request, next_start_age,prediction_history } = response.data;
             
                    // 更新现有属性
                    this.start_age = next_start_age;
                    this.prediction_history = prediction_history;

                     // 渲染结果
                    const rawJsonStr = prediction.replace("</json>", "").replace("<json>", "");
                    const jsonArr = JSON.parse(rawJsonStr);
                    jsonArr.map(item => {
                        item.text = `age${item.age}: ${item.event}`;
                    });
                    this.predictions.push(...jsonArr);
            
                    console.log(this.predictions);
                    console.log(this.dead_age)
                    
                    if(continue_request) {
                        this.fetchPrediction();
                    } else {
                        this.isLoading = false;
                        this.restartGame = true;
                    }
                } catch(error) {
                    console.error(error);
                    this.fetchPrediction();
                }
            },
            resetGame() {
                this.predictions = [];
                this.isLoading = true;
                this.restartGame = false;
                this.prediction_history = '';
                
                this.$router.push({ name: 'StartPage' });
            }
        },
    };
</script>



<style scoped>
    .page_container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        height:  80vh;
    }

    .predict_box{
        width: 1200px;
        min-height: 50px;
        font-weight:normal;
        font-size: 18px;
        border: 1px solid #000000;
        border-radius: 10px;
        margin-top: 15px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding-left: 20px; 
        text-align: left;
    }

    .main_button {
        margin-top: 20px;
    }

</style>
