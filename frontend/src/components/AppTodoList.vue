<template lang="html">
    <div>
        <!-- Todo list section -->
        <div class="row mx-1 px-5 pb-3 w-80">
            <div class="col mx-auto">
                <!-- Todo Item 1 -->
                <div class="row px-3 align-items-center todo-item rounded">
                    <div class="col-auto m-1 p-0 d-flex align-items-center">
                        <h2 class="m-0 p-0">
                            <i class="fa fa-square-o text-primary btn m-0 p-0 d-none" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as complete"></i>
                            <i class="fa fa-check-square-o text-primary btn m-0 p-0" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as todo"></i>
                        </h2>
                    </div>
                    <div class="col px-1 m-1 d-flex align-items-center">
                        <input type="text"
                            class="form-control form-control-lg border-0 edit-todo-input bg-transparent rounded px-3"
                            readonly value="Buy groceries for next week" title="Buy groceries for next week" />
                        <input type="text"
                            class="form-control form-control-lg border-0 edit-todo-input rounded px-3 d-none"
                            value="Buy groceries for next week" />
                    </div>
                    <div class="col-auto m-1 p-0 px-3 d-none">
                    </div>
                    <div class="col-auto m-1 p-0 todo-actions">
                        <div class="row d-flex align-items-center justify-content-end">
                            <h5 class="m-0 p-0 px-2">
                                <i class="fa fa-pencil text-info btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Edit todo"></i>
                            </h5>
                            <h5 class="m-0 p-0 px-2">
                                <i class="fa fa-trash-o text-danger btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Delete todo"></i>
                            </h5>
                        </div>
                        <div class="row todo-created-info">
                            <div class="col-auto d-flex align-items-center pr-2">
                                <i class="fa fa-info-circle my-2 px-2 text-black-50 btn" data-toggle="tooltip"
                                    data-placement="bottom" title="" data-original-title="Created date"></i>
                                <label class="date-label my-2 text-black-50">28th Jun 2020</label>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Todo Item 2 -->
                <div class="row px-3 align-items-center todo-item rounded">
                    <div class="col-auto m-1 p-0 d-flex align-items-center">
                        <h2 class="m-0 p-0">
                            <i class="fa fa-square-o text-primary btn m-0 p-0" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as complete"></i>
                            <i class="fa fa-check-square-o text-primary btn m-0 p-0 d-none" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as todo"></i>
                        </h2>
                    </div>
                    <div class="col px-1 m-1 d-flex align-items-center">
                        <input type="text"
                            class="form-control form-control-lg border-0 edit-todo-input bg-transparent rounded px-3"
                            readonly value="Renew car insurance" title="Renew car insurance" />
                        <input type="text"
                            class="form-control form-control-lg border-0 edit-todo-input rounded px-3 d-none"
                            value="Renew car insurance" />
                    </div>
                    <div class="col-auto m-1 p-0 px-3">
                        <div class="row">
                            <div class="col-auto d-flex align-items-center rounded bg-white border border-warning">
                                <i class="fa fa-hourglass-2 my-2 px-2 text-warning btn" data-toggle="tooltip"
                                    data-placement="bottom" title="" data-original-title="Due on date"></i>
                                <h6 class="text my-2 pr-2">28th Jun 2020</h6>
                            </div>
                        </div>
                    </div>
                    <div class="col-auto m-1 p-0 todo-actions">
                        <div class="row d-flex align-items-center justify-content-end">
                            <h5 class="m-0 p-0 px-2">
                                <i class="fa fa-pencil text-info btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Edit todo"></i>
                            </h5>
                            <h5 class="m-0 p-0 px-2">
                                <i class="fa fa-trash-o text-danger btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Delete todo"></i>
                            </h5>
                        </div>
                        <div class="row todo-created-info">
                            <div class="col-auto d-flex align-items-center pr-2">
                                <i class="fa fa-info-circle my-2 px-2 text-black-50 btn" data-toggle="tooltip"
                                    data-placement="bottom" title="" data-original-title="Created date"></i>
                                <label class="date-label my-2 text-black-50">28th Jun 2020</label>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Todo Item 3 -->
                <div class="row px-3 align-items-center todo-item editing rounded">
                    <div class="col-auto m-1 p-0 d-flex align-items-center">
                        <h2 class="m-0 p-0">
                            <i class="fa fa-square-o text-primary btn m-0 p-0" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as complete"></i>
                            <i class="fa fa-check-square-o text-primary btn m-0 p-0 d-none" data-toggle="tooltip"
                                data-placement="bottom" title="Mark as todo"></i>
                        </h2>
                    </div>
                    <div class="col px-1 m-1 d-flex align-items-center">
                        <input type="text"
                            class="form-control form-control-lg border-0 edit-todo-input bg-transparent rounded px-3 d-none"
                            readonly value="Sign up for online course" title="Sign up for online course" />
                        <input type="text" class="form-control form-control-lg border-0 edit-todo-input rounded px-3"
                            value="Sign up for online course" />
                    </div>
                    <div class="col-auto m-1 p-0 px-3 d-none">
                    </div>
                    <div class="col-auto m-1 p-0 todo-actions">
                        <div class="row d-flex align-items-center justify-content-end">
                            <h5 class="m-0 p-0 px-2 edit-icon">
                                <i class="fa fa-pencil text-info btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Edit todo"></i>
                            </h5>
                            <h5 class="m-0 p-0 px-2">
                                <i class="fa fa-trash-o text-danger btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Delete todo"></i>
                            </h5>
                        </div>
                        <div class="row todo-created-info">
                            <div class="col-auto d-flex align-items-center pr-2">
                                <i class="fa fa-info-circle my-2 px-2 text-black-50 btn" data-toggle="tooltip"
                                    data-placement="bottom" title="" data-original-title="Created date"></i>
                                <label class="date-label my-2 text-black-50">28th Jun 2020</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    components: {

    }
}
</script>

<style lang="css" scoped>
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