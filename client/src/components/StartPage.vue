<template>
    <div class="container"> 
        <h1 class="title">Life Predict</h1>
        <p class="description">
            Experience the simulation of lives from different backgrounds.
        </p>
        <div class="author">by: xiahan夏晗</div>
        <comfirm-button class="main_button" text="Start Game" @click="goToNextPage" />
    </div>
</template>

<script>
    import ComfirmButton from './ComfirmButton.vue';

    export default {
        name: "StartPage",
        components: {
            ComfirmButton 
        },
        methods: {
            goToNextPage() {
                this.$router.push({ name: 'ChooseStyle' });
            }
        },
    }

    
</script>

<style scoped>
    .container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height:  80vh;
    }

    .title {
        font-family: 'Inter';
        font-style: italic;
        font-weight: 800;
        font-size: 111px;
        line-height: 134px;
        color: #333333;
    }

    .description{
        font-family: 'Inter';
        font-style: italic;
        font-weight: 400;
        font-size: 34px;
        line-height: 41px
    }

    .author {
        font-family: 'Inter';
        font-style: italic;
        font-weight: 400;
        font-size: 24px;
        line-height: 29px;
        color: #333333;
    }

    .main_button {
        margin-top: 200px;
    }

</style>
