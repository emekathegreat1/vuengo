<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view />
  <router-link to="/"> </router-link>
</template>

<style lang="scss">
@import "../node_modules/bulma";

nav {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 5px;
}
</style>
