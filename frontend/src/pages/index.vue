<script setup>
import { onBeforeUnmount, ref } from 'vue';
import {useWebSocket} from '@vueuse/core';

const { status, data, send, open, close } = useWebSocket('ws://localhost:8001/ws/', {
    onMessage(ws, e) { cum_data.value += JSON.parse(e.data).message + '\n'; }
})

const cum_data = ref("");
const msg = ref("");

function send_msg() {
    send(JSON.stringify({ message: msg.value }))
}

</script>

<template>
    <form @submit.prevent="send_msg">
        <fieldset role="group">
            <input v-model="msg" type="text">
            <button>Submit</button>
        </fieldset>
    </form>
    <pre>{{ cum_data }}</pre>
</template>
