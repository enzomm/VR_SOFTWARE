<script setup lang="ts">
import type { Table } from '@tanstack/vue-table'
import type { Product, NewProduct } from '@/data/schema'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { X, Tag } from "lucide-vue-next"
import { computed } from 'vue'
import { types } from '@/data/data'
import DataTableFacetedFilter from './DataTableFacetedFilter.vue'
import DataTableViewOptions from './DataTableViewOptions.vue'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger
} from '@/components/ui/dialog'
import {
  Drawer,
  DrawerClose,
  DrawerContent,
  DrawerDescription,
  DrawerFooter,
  DrawerHeader,
  DrawerTitle,
  DrawerTrigger
} from '@/components/ui/drawer'
import {
  createReusableTemplate,
  useMediaQuery
} from '@vueuse/core'
import { ref } from 'vue'
import { toast } from '@/components/ui/toast/use-toast'
import { h } from 'vue'
import ProductForm from '@/components/ProductForm.vue'
import { createProduct } from '@/lib/api'

const readFileAsBase64 = (file: File): Promise<string> => {
  return new Promise((resolve) => {
    const reader = new FileReader()
    reader.onload = () => {
      resolve(reader.result as string)
    }
    reader.readAsDataURL(file)
  })
}

const onSubmit = async (values: any) => {
  const selectedImage = values.image as File
  let base64Image = ""
  if (selectedImage) {
    base64Image = await readFileAsBase64(selectedImage)
  }

  const createdProduct: NewProduct = {    
    image: base64Image,
    description: values.description,
    cost: values.cost.toString(),
    type: values.type,
  }

  await createProduct(createdProduct)
  
  toast({
    title: 'You submitted the following values:',
    description: h('pre', { class: 'mt-2 w-[340px] rounded-md bg-slate-950 p-4' }, h('code', { class: 'text-white' }, JSON.stringify(values, null, 2))),
  })

  isOpen.value = false
}

const [UseTemplate, CreateForm] = createReusableTemplate()

const isDesktop = useMediaQuery('(min-width: 768px)')

const isOpen = ref(false)

interface DataTableToolbarProps {
  table: Table<Product>
}

const props = defineProps<DataTableToolbarProps>()

const isFiltered = computed(() => props.table.getState().columnFilters.length > 0)
</script>

<template>
  <div class="flex items-center justify-between">
    <div class="flex flex-1 items-center space-x-2">
      <Input
        placeholder="Filter codes..."
        :model-value="(table.getColumn('id')?.getFilterValue() as string) ?? ''"
        class="h-8 w-[150px] lg:w-[250px]"
        @input="table.getColumn('id')?.setFilterValue($event.target.value)"
      />   
      <DataTableFacetedFilter
        v-if="table.getColumn('type')"
        :column="table.getColumn('type')"
        title="Type"
        :options="types"
      />   
      
      <UseTemplate>
        <ProductForm :onSubmit="onSubmit" />
      </UseTemplate>

      <Dialog v-if="isDesktop" v-model:open="isOpen">
        <DialogTrigger as-child>
          <Button id="create-button-product-form-dialog" class="h-8">
            <Tag class="mr-2 h-4 w-4" />
            Add Product
          </Button>
        </DialogTrigger>
        <DialogContent class="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Edit profile</DialogTitle>
            <DialogDescription>
              Make changes to your profile here. Click save when you're done.
            </DialogDescription>
          </DialogHeader>
          <CreateForm />
        </DialogContent>
      </Dialog>

      <Drawer v-else v-model:open="isOpen">
        <DrawerTrigger as-child>
          <Button id="create-button-product-form-drawer" class="h-8">
            <Tag class="mr-2 h-4 w-4" />
            Add Product
          </Button>
        </DrawerTrigger>
        <DrawerContent>
          <DrawerHeader class="text-left">
            <DrawerTitle>Edit profile</DrawerTitle>
            <DrawerDescription>
              Make changes to your profile here. Click save when you're done.
            </DrawerDescription>
          </DrawerHeader>
          <CreateForm />
          <DrawerFooter class="pt-2">
            <DrawerClose as-child>
              <Button variant="outline">
                Cancel
              </Button>
            </DrawerClose>
          </DrawerFooter>
        </DrawerContent>
      </Drawer>

      <Button
        v-if="isFiltered"
        variant="ghost"
        class="h-8 px-2 lg:px-3"
        @click="table.resetColumnFilters()"
      >
        Reset
        <X class="ml-2 h-4 w-4" />
      </Button>
    </div>
    <DataTableViewOptions :table="table" />
  </div>
</template>
