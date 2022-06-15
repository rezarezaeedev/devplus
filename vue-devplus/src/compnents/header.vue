<script>
export default{
    props:['data']
}
</script>

<template>
    <header class="text-center text-myblack  bg-gradient-to-r from-cyan-500 to-green-500 py-28 mb-12 shadow-sm shadow-green-700 ">
        <div class="w-3/12 divide-y-2 divide-myblack mx-auto space-y-3 " > 
            <h1 class="text-6xl font-bold  hover:animate-bounce ease-in-out transition-all delay-300 duration-500">{{data.title}}</h1>
            <h2 class='text-2xl'>{{data.admin_name}}</h2>
        </div>
    </header>
</template>