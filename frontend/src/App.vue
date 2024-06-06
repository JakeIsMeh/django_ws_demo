<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <main><RouterView /></main>
</template>

<style lang="scss">
@use "@picocss/pico/scss" with (
	/* Pico settings */
	$theme-color: "pink",
	$semantic-root-element: "#app",
	$enable-semantic-container: true,
);
@use "@picocss/pico/scss/colors/utilities" with (
	/* Prefix for CSS variables */
	$css-class-prefix: "",

	$properties: (
		/* Class name prefixes */
		"color": "c",
		"background-color": "bg",
	),
);

:root {
	--pico-spacing: 0.5rem;
	--pico-form-element-spacing-vertical: 0.5rem;
	--pico-form-element-spacing-horizontal: 0.75rem;
}
</style>
