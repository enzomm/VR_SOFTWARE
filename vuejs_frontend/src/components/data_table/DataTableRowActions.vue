<script setup lang="ts">
import { Button } from '@/components/ui/button'
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
import { ref, computed, watch } from 'vue'
import { DropdownMenuItem } from '@/components/ui/dropdown-menu'
import DropdownMenuComponent from './DropdownMenu.vue'
import Toaster from '@/components/ui/toast/Toaster.vue'
import { toast } from '@/components/ui/toast/use-toast'
import { h } from 'vue'
import type { Row } from '@tanstack/vue-table'
import type { Product } from '@/data/schema'
import { productSchema } from '@/data/schema'
import { deleteProduct, updateProduct, fetchProduct } from '@/lib/api'
import ProductForm from '@/components/ProductForm.vue'

interface DataTableRowActionsProps {
  row: Row<Product>
}
const props = defineProps<DataTableRowActionsProps>()

const product = computed(() => productSchema.parse(props.row.original))

const deleteRow = async () => {
  await deleteProduct(product.value.id)
}

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

  const updatedProduct: Product = {
    id: product.value.id.toString(),
    image: base64Image,
    description: values.description,
    cost: values.cost.toString(),
    type: values.type,
  }

  await updateProduct(updatedProduct)
  
  toast({
    title: 'You submitted the following values:',
    description: h('pre', { class: 'mt-2 w-[340px] rounded-md bg-slate-950 p-4' }, h('code', { class: 'text-white' }, JSON.stringify(values, null, 2))),
  })

  isOpen.value = false
}

const productToEdit = ref<Product | null>(null)

const fetchProductDetails = async (id: string) => {  
  const product = await fetchProduct(id)
  productToEdit.value = product
}

const [UseTemplate, EditForm] = createReusableTemplate()

const isDesktop = useMediaQuery('(min-width: 768px)')

const isOpen = ref(false)

watch(isOpen, async (newVal) => {
  if (newVal && product.value.id) {
    await fetchProductDetails(product.value.id)
  }
})
</script>

<template>
  <UseTemplate>
    <ProductForm :onSubmit="onSubmit" :initialValues="productToEdit ? {
      image: productToEdit.image,
      description: productToEdit.description,
      cost: parseFloat(productToEdit.cost),
      type: productToEdit.type
    } : {}" />
  </UseTemplate>

  <Dialog v-if="isDesktop" v-model:open="isOpen">

    <DropdownMenuComponent :deleteRow="deleteRow">
      <template #trigger-item>
        <DialogTrigger as-child>
          <DropdownMenuItem>Edit</DropdownMenuItem>
        </DialogTrigger>
      </template>
    </DropdownMenuComponent>

    <DialogContent class="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Edit product</DialogTitle>
        <DialogDescription>
          Make changes to your product here. Click save when you're done.
        </DialogDescription>
      </DialogHeader>
      <EditForm />
    </DialogContent>
  </Dialog>

  <Drawer v-else v-model:open="isOpen">

    <DropdownMenuComponent :deleteRow="deleteRow">
      <template #trigger-item>
        <DrawerTrigger as-child>
          <DropdownMenuItem>Edit</DropdownMenuItem>
        </DrawerTrigger>
      </template>
    </DropdownMenuComponent>

    <DrawerContent>
      <DrawerHeader class="text-left">
        <DrawerTitle>Edit product</DrawerTitle>
        <DrawerDescription>
          Make changes to your product here. Click save when you're done.
        </DrawerDescription>
      </DrawerHeader>
      <EditForm />
      <DrawerFooter class="pt-2">
        <DrawerClose as-child>
          <Button variant="outline">Cancel</Button>
        </DrawerClose>
      </DrawerFooter>
    </DrawerContent>
  </Drawer>

  <Toaster />
</template>
