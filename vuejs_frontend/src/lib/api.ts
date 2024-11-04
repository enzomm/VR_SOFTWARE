import { ref } from 'vue'
import axios from 'axios'
import type { Product, NewProduct } from '@/data/schema'

const baseURL = 'http://127.0.0.1:5000'
const products = ref<Product[]>([])

const fetchProducts = async () => {
  try {
    const response = await axios.get(`${baseURL}/get_products`)
    products.value = response.data
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error searching for products:', error.response?.data?.message)
    } else {
      console.error('Unknown error:', error)
    }
  }
}

const fetchProduct = async (id: string) => {
  try {
    const response = await axios.get(`${baseURL}/get_product/${id}`)
    return response.data
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error searching for product:', error.response?.data?.message)
    } else {
      console.error('Unknown error:', error)
    }   
  }
}

const createProduct = async (product: NewProduct) => {
  try {
    await axios.post(`${baseURL}/set_product`, product)
    await fetchProducts()
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error creating product:', error.response?.data?.message)
    } else {
      console.error('Unknown error:', error)
    }
  }
}

const updateProduct = async (product: Product) => {
  try {
    await axios.post(`${baseURL}/update_product`, product)
    await fetchProducts()
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error updating product:', error.response?.data?.message)
    } else {
      console.error('Unknown error:', error)
    }
  }
}

const deleteProduct = async (id: string) => {
  try {
    await axios.delete(`${baseURL}/delete_product/${id}`)
    await fetchProducts()
  } catch (error: unknown) {
    if (axios.isAxiosError(error)) {
      console.error('Error deleting product:', error.response?.data?.message)
    } else {
      console.error('Unknown error:', error)
    }
  }
}

export { products, fetchProducts, createProduct, updateProduct, deleteProduct, fetchProduct }
