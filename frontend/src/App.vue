<template>
    <div id="app">
        <app-header></app-header>
        <div class="container m-5 p-2 rounded mx-auto bg-light shadow">
            <app-title></app-title>
            <app-todo-add></app-todo-add>
            <div class="p-2 mx-4 border-black-25 border-bottom"></div>
            <app-todo-filter></app-todo-filter>
            <app-todo-list></app-todo-list>
        </div>
    </div>
</template>

<script>
import AppHeader from './components/AppHeader.vue'
import AppTitle from './components/AppTitle.vue'
import AppTodoAdd from './components/AppTodoAdd.vue'
import AppTodoFilter from './components/AppTodoFilter.vue'
import AppTodoList from './components/AppTodoList.vue'

export default {
    name: 'App',
    components: {
        AppHeader,
        AppTitle,
        AppTodoAdd,
        AppTodoFilter,
        AppTodoList
    }
}
</script>

<style>
body {
    font-family: "Open Sans", sans-serif;
    line-height: 1.6;
}

.add-todo-input,
.edit-todo-input {
    outline: none;
}

.add-todo-input:focus,
.edit-todo-input:focus {
    border: none !important;
    box-shadow: none !important;
}

.view-opt-label,
.date-label {
    font-size: 0.8rem;
}

.edit-todo-input {
    font-size: 1.7rem !important;
}

.todo-actions {
    visibility: hidden !important;
}

.todo-item:hover .todo-actions {
    visibility: visible !important;
}

.todo-item.editing .todo-actions .edit-icon {
    display: none !important;
}
</style>
