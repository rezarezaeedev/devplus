
<script>
export default{
    props:['data']
}
</script>

<template>
    <footer class="relative opacity-90 text-lg   w-full mt-32 text-center text-myblack  bg-gradient-to-r from-cyan-500 to-green-500 shadow-sm shadow-green-700 flex flex-col justify-center items-center space-y-3 ">
        <p class="p-2">{{data.buildtext}} <span class="text-sm">{{data.fortext}} </span></p>
        <p class="absolute right-5 bottom-3 text-xs">{{data.copyright}} </p>
    </footer>
</template>

