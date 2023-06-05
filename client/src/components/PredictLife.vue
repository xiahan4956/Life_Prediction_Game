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
        data() {
            return {
                predictions: [],
                isLoading: true,
                restartGame: false,
                prediction_history: ''
            };
        },
        methods: {
            async fetchPrediction() {
                try {
                    const response = await this.$http.post('http://qq4956.pythonanywhere.com/api/predict', { prediction_history: this.prediction_history });
                    const { prediction, continue_request, prediction_history } = response.data;
             
                    // eslint-disable-next-line no-debugger
                    // debugger;
                    
                     // 将prediction转换为JSON对象
                    const rawJsonStr = prediction.replace("</json>", "").replace("<json>", "");
                    const jsonArr = JSON.parse(rawJsonStr);

                    jsonArr.map(item => {
                        item.text = `${item.age}: ${item.event}`;
                    });

                    this.predictions.push(...jsonArr);
                    this.prediction_history = prediction_history;

    
                    console.log(this.predictions);
                    
                

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
        mounted() {
            this.fetchPrediction();
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
