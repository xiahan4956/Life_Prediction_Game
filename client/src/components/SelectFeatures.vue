<template>
    <div class="page_container"> 
        <h1 class="title">Choose your feature(3/3)</h1>
  
        <div class="feature-main-container">
            <feature-component v-for="(feature, index) in potentialFeatures" 
                               :key="index" 
                               :feature="feature" 
                               @selected="featureSelected" 
                               @deselected="featureDeselected"></feature-component>
        </div>
  
        <comfirm-button class="comfirm-button" text="Next" @click="send_features"/>
    </div>
</template>
  
<script>
import ComfirmButton from './ComfirmButton.vue';
import FeatureComponent from './FeatureComponent.vue';
import axios from 'axios';

export default {
    name: "SelectFeatures",
    components: {
        ComfirmButton,
        FeatureComponent
    },
    data() {
        return {
            potentialFeatures: [],
            selectedFeatures: [],
        }
    },
    methods: {
        featureSelected(feature) {
            if (this.selectedFeatures.length < 3) {
                this.selectedFeatures.push(feature);
            }
        },
        featureDeselected(feature) {
            if (this.selectedFeatures.includes(feature)) {
                let index = this.selectedFeatures.indexOf(feature);
                this.selectedFeatures.splice(index, 1);
    }
        },
        async send_features() {
            if (this.selectedFeatures.length > 0) {
                const response = await axios.post('http://qq4956.pythonanywhere.com/api/selected_features', {
                    selected_features: this.selectedFeatures
                });
                if (response.data.msg === 'features received') {
                    this.$router.push({ name: 'PredictLife' });
                }
                else {
                    alert("Something went wrong");
                }
            } 
            else {
                alert("Please select at least one feature");
            }
        },
    },
    mounted() {
        this.potentialFeatures = JSON.parse(localStorage.getItem('potentialFeatures'));
    },
};

</script>

<style scoped>
    .page_container{
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

    .feature-main-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    .comfirm-button{
        margin-top: 20px;
    }


</style>
