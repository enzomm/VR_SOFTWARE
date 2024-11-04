<script setup lang="ts">
import { onMounted } from 'vue'
import { products, fetchProducts } from '@/lib/api'
import { columns } from '@/components/data_table/columns'
import DataTable from '@/components/data_table/DataTable.vue'

onMounted(() => {
  fetchProducts()
})
</script>

<template>
  <DataTable :data="products" :columns="columns" />
</template>

<style scoped>
</style>
