
<script>
export default{
    props:['data']
}
</script>

<template>
    <div class="mx-auto mb-20"> <!--Post Item-->
        <img class="w-7/12 h-96 mx-auto mt-5 mb-10 rounded-lg  object-cover shadow-sm shadow-myblack"  :src="data.image" :alt="data.title+' - '+data.author">
        <p class="text-lg w-8/12 mx-auto "></p>
        <div class="text-lg w-8/12 mx-auto ">
                    <p>{{data.content}}</p>
                    <h4 class="text-base text-myblack text-lg opacity-70 py-1"><em>{{data.author}}</em></h4>   
                </div>
        <div class="w-8/12 mx-auto my-2">
            <button type="submit" class="font-semibold rounded-sm bg-gradient-to-r from-blue-500 to-blue-400 text-lg text-myblack px-3 py-2 text-center">More ...</button>            
        </div>            
    </div>
</template>





