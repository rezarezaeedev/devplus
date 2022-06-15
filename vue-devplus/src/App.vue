<script>
import axios from './apis/axios';
import { defineAsyncComponent } from 'vue';

export default{
    data(){
        return{
            siteinfo:{},
            posts:[],
        }
    },

    created(){
        this.load_posts();
        this.load_siteinfo();
    },

    methods:{
        load_posts(){
            axios.get('posts')
            .then(res=>{
                this.posts=res.data
            })
            .catch(err=>console.log(`Error: -${err}`))
        },

        load_siteinfo(){
                    axios.get('siteinfo')
            .then(res=>{
                this.siteinfo=res.data
            })
            .catch(err=>console.log(`Error: -${err}`))
        },
    },

    components:{
        'devplus-header':defineAsyncComponent(()=>import('./compnents/header.vue')),
        'devplus-footer':defineAsyncComponent(()=>import('./compnents/footer.vue')),
        'devplus-post':defineAsyncComponent(()=>import('./compnents/post.vue')),
    }
}
</script>

<template>
    <devplus-header :data="siteinfo"></devplus-header>
    <main class="container w-8/12 mx-auto text-6xl py-5 ">
        <div class='space-y-36 divide-dotted divide-y-2 divide-myblack'> <!--POst list-->
            <devplus-post v-for="item in posts" :key="item.id" :data="item"></devplus-post>
        </div>
    </main>
    <devplus-footer :data="siteinfo"></devplus-footer>
    
</template>

<style>
</style>
