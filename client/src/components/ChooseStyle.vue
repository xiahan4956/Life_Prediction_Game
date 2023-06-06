<template>
    <div class="page_container"> 
        <h1 class="title">Choose a game style(1/3)</h1>
        <div class = "sytle_container">
        <button v-for="style in game_styles" :key="style" class="game_style" @click="selectStyle(style)">{{ style }}</button>
        </div>
        <comfirm-button  class="main_button" text="Next" @click="confirmStyle" :disabled="!selectedStyle" />
    </div>
</template>

<script>
    import ComfirmButton from './ComfirmButton.vue';

    export default {
        name: "ChooseStyle",
        components: {
            ComfirmButton 
        }, 
        data() {
        return {
            game_styles: ['Real', 'Fantasy', 'Cyber punk', 'Medieval', 'Sci-Fi'],
            selectedStyle: null,
        };
        },

        methods: {
            selectStyle(style) {
                this.selectedStyle = style;
            },
            confirmStyle() {
                // 有selectedStyle才跳转,没有就弹窗选择
                if (this.selectedStyle) {
                        this.$router.push({ name: 'SelectAttribute', params: { feature: this.selectedStyle } });
                        window.localStorage.setItem('selectedStyle', this.selectedStyle);
                } else {
                    alert("Please select a game style before proceeding.");
                }
    },
        }
        
    };
</script>

<style scoped>
    .page_container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height:  80vh;
    }


    .title {
        font-weight: 400;
        font-size: 80px;
        line-height: 24px;
        color: #333333;
    }

    .sytle_container{
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height:  80vh;
    }

    .game_style{
        /* 增加外边框,外框大一些 */
        padding: 10px 30px;
        margin: 10px;
        border: 2px solid #000000;
        border-radius:9px;
        font-size: 20px;
        width: 400px;
        background-color: #FFFFFF
    }

    .game_style:hover {
        background-color: #CCCCCC;
    }

    .game_style:focus {
        background-color: #CCCCCC;
    }


    .main_button{
        margin-top: 20px;
    }

</style>
